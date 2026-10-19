from django.db import models
from django.core.exceptions import ValidationError
from usuarios.models import Usuario

# --- POO: CLASE ABSTRACTA (HERENCIA) ---
class ModeloBase(models.Model):
    """Clase base abstracta con lógica reusable de auditoría."""
    FechaCreacion = models.DateTimeField(auto_now_add=True, db_column='FechaCreacion')

    class Meta:
        abstract = True


# 1. Categoria
class Categoria(models.Model):
    IdCategoria = models.AutoField(primary_key=True, db_column='IdCategoria')
    NombreCategoria = models.CharField(max_length=40, unique=True, db_column='NombreCategoria')
    Descripcion = models.CharField(max_length=250, db_column='Descripcion')

    class Meta:
        db_table = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.NombreCategoria


# 2. ReporteAmbiental (Hereda de ModeloBase)
class ReporteAmbiental(ModeloBase):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Resuelto', 'Resuelto'),
        ('Rechazado', 'Rechazado'),
    ]

    IdReporteAmbiental = models.AutoField(primary_key=True, db_column='IdReporteAmbiental')
    Titulo = models.CharField(max_length=90, db_column='Titulo')
    Descripcion = models.TextField(db_column='Descripcion')
    UbicacionReferencial = models.CharField(max_length=200, db_column='UbicacionReferencial')
    Latitud = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True, db_column='Latitud')
    Longitud = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True, db_column='Longitud')
    Estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente', db_column='Estado')
    
    IdUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='IdUsuario', related_name='reportes')
    IdCategoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, db_column='IdCategoria')

    class Meta:
        db_table = 'ReporteAmbiental'

    # --- POO: MÉTODOS DE NEGOCIO Y POLIMORFISMO ---
    def cambiar_estado(self, nuevo_estado, usuario_admin, observacion=""):
        """Método de negocio para transicionar de estado y registrar auditoría."""
        estados_validos = [e[0] for e in self.ESTADOS]
        if nuevo_estado not in estados_validos:
            raise ValidationError(f"Estado '{nuevo_estado}' no es válido.")

        estado_anterior = self.Estado
        self.Estado = nuevo_estado
        self.save()

        # Registrar automáticamente en el historial (Composición)
        HistorialEstado.objects.create(
            EstadoAnterior=estado_anterior,
            EstadoNuevo=nuevo_estado,
            Observacion=observacion,
            IdReporteAmbiental=self,
            IdUsuarioAdmin=usuario_admin
        )

    def es_prioritario(self):
        """Métrica de negocio: determina si el reporte es crítico."""
        palabras_clave = ['fuga', 'contaminacion', 'peligro', 'veneno', 'emergencia']
        return any(p in self.Descripcion.lower() for p in palabras_clave)

    def __str__(self):
        return f"[{self.Estado}] {self.Titulo}"


# 3. EvidenciaFotografia
class EvidenciaFotografia(models.Model):
    IdEvidenciaFotografia = models.AutoField(primary_key=True, db_column='IdEvidenciaFotografia')
    RutaArchivo = models.CharField(max_length=255, db_column='RutaArchivo')
    FechaCarga = models.DateTimeField(auto_now_add=True, db_column='FechaCarga')
    Tamano = models.BigIntegerField(null=True, blank=True, db_column='Tamano')
    IdReporteAmbiental = models.ForeignKey(ReporteAmbiental, on_delete=models.CASCADE, db_column='IdReporteAmbiental', related_name='evidencias')

    class Meta:
        db_table = 'EvidenciaFotografia'


# 4. HistorialEstado
class HistorialEstado(models.Model):
    IdHistorialEstado = models.AutoField(primary_key=True, db_column='IdHistorialEstado')
    EstadoAnterior = models.CharField(max_length=20, db_column='EstadoAnterior')
    EstadoNuevo = models.CharField(max_length=20, db_column='EstadoNuevo')
    Observacion = models.CharField(max_length=255, null=True, blank=True, db_column='Observacion')
    FechaCambio = models.DateTimeField(auto_now_add=True, db_column='FechaCambio')
    IdReporteAmbiental = models.ForeignKey(ReporteAmbiental, on_delete=models.CASCADE, db_column='IdReporteAmbiental')
    IdUsuarioAdmin = models.ForeignKey(Usuario, on_delete=models.PROTECT, db_column='IdUsuarioAdmin')

    class Meta:
        db_table = 'HistorialEstado'