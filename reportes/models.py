from django.db import models

class Rol(models.Model):
    IdRol = models.AutoField(primary_key=True, db_column='IdRol')
    NombreRol = models.CharField(max_length=50, unique=True, db_column='NombreRol')
    Descripcion = models.CharField(max_length=250, db_column='Descripcion')

    class Meta:
        db_table = 'Roles'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.NombreRol


class Usuario(models.Model):
    IdUsuario = models.AutoField(primary_key=True, db_column='IdUsuario')
    Nombre = models.CharField(max_length=50, db_column='Nombre', default='')
    Apellido = models.CharField(max_length=60, db_column='Apellido', default='')
    Correo = models.CharField(max_length=150, unique=True, db_column='Correo')
    Contraseña = models.CharField(max_length=150, db_column='Contraseña', default='')
    Telefono = models.CharField(max_length=20, blank=True, null=True, db_column='Telefono')
    FechaRegistro = models.DateTimeField(auto_now_add=True, db_column='FechaRegistro')
    Activo = models.BooleanField(default=True, db_column='Activo')

    IdRol = models.ForeignKey(Rol, on_delete=models.PROTECT, db_column='IdRol')

    class Meta:
        db_table = 'Usuarios'

    def __str__(self):
        return f"{self.Nombre} {self.Apellido} ({self.Correo})"
    
# 3. Categoria
class Categoria(models.Model):
    IdCategoria = models.AutoField(primary_key=True)
    NombreCategoria = models.CharField(max_length=40, unique=True)
    Descripcion = models.CharField(max_length=250)

    class Meta:
        db_table = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.NombreCategoria


# 4. ReporteAmbiental
class ReporteAmbiental(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Resuelto', 'Resuelto'),
        ('Rechazado', 'Rechazado'),
    ]

    IdReporteAmbiental = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=90)
    Descripcion = models.TextField()
    UbicacionReferencial = models.CharField(max_length=200)
    Latitud = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    Longitud = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    Estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    FechaCreacion = models.DateTimeField(auto_now_add=True)
    
    IdUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='IdUsuario', related_name='reportes')
    IdCategoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, db_column='IdCategoria')

    class Meta:
        db_table = 'ReporteAmbiental'

    def __str__(self):
        return f"[{self.Estado}] {self.Titulo}"


# 5. EvidenciaFotografia
class EvidenciaFotografia(models.Model):
    IdEvidenciaFotografia = models.AutoField(primary_key=True)
    RutaArchivo = models.CharField(max_length=255)
    FechaCarga = models.DateTimeField(auto_now_add=True)
    Tamano = models.BigIntegerField(null=True, blank=True)
    IdReporteAmbiental = models.ForeignKey(ReporteAmbiental, on_delete=models.CASCADE, db_column='IdReporteAmbiental', related_name='evidencias')

    class Meta:
        db_table = 'EvidenciaFotografia'


# 6. HistorialEstado
class HistorialEstado(models.Model):
    IdHistorialEstado = models.AutoField(primary_key=True)
    EstadoAnterior = models.CharField(max_length=20)
    EstadoNuevo = models.CharField(max_length=20)
    Observacion = models.CharField(max_length=255, null=True, blank=True)
    FechaCambio = models.DateTimeField(auto_now_add=True)
    
    IdReporteAmbiental = models.ForeignKey(ReporteAmbiental, on_delete=models.CASCADE, db_column='IdReporteAmbiental')
    IdUsuarioAdmin = models.ForeignKey(Usuario, on_delete=models.PROTECT, db_column='IdUsuarioAdmin')

    class Meta:
        db_table = 'HistorialEstado'