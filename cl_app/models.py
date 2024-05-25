from django.db import models
from autoslug.fields import AutoSlugField

class Entidad(models.Model):
    nombre = models.CharField('Nombre',max_length=200, blank=False, null = True)
    direccion = models.CharField('Dirección',null=True, blank=False, max_length=200)
    telefono = models.CharField('Teléfono', null=True, blank=False, max_length=200)
    cuentaCUP = models.CharField('Cuenta CUP', null=True, blank=True, max_length=50)
    titularCUP = models.CharField('Titular Cuenta CUP',blank=True, null = True, max_length=200)
    cuentaCL = models.CharField('Cuenta CL',blank=False, null = True, max_length=50)
    titularCL = models.CharField('Titular Cuenta CL', blank=False, null = True, max_length=200)
    bancoCUP = models.CharField('Banco CUP', blank=False, null = True, max_length=200)
    cuentaEst = models.CharField('Cuenta Estandarizada', null=True, blank=False, max_length=50)
    vigencia = models.IntegerField('Vigencia de Oferta', blank=True, null = True)
    margen = models.DecimalField('Margen CL', max_digits=5, decimal_places=2, blank=False, null = True)

    class Meta:
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
     nombre = models.CharField('Nombre de la Categoría',max_length=200, blank=False, null = False)
     habilitada = models.BooleanField('Categoría Activada/Categoría no Activada', default = True)
     margporc = models.BooleanField('Margen/Porciento')
     valormag = models.DecimalField('Valor del Margen Comercial CUP', max_digits=5, decimal_places=2, null=False, blank=False)
     #slug = models.SlugField(max_length=255, blank=False, null = True, unique=True
     slug = AutoSlugField(populate_from='nombre', always_update=True, unique=True)

     class Meta:
         verbose_name = 'Categoría'
         verbose_name_plural = 'Categorías'

     def __str__(self):
        return self.nombre

class Cliente(models.Model):
    OCCIDENTE = "OCC"
    CENTRO = "CEN"
    ORIENTE = "ORI"
    PVenta = {
        OCCIDENTE: "Occidente",
        CENTRO: "Centro",
        ORIENTE: "Oriente",
    }

    nombre = models.CharField('Nombre',max_length=250, blank=False, null = False)
    codigo = models.CharField('Codigo',max_length=50, blank=False, null = False)
    direccion = models.CharField('Direccion',max_length=250, blank=True, null = True)
    Telefono = models.CharField(max_length=50, blank=True, null = True)
    Provincia = models.CharField(max_length=80,choices=PVenta, blank=False, null = False)
    correo = models.EmailField('Correo electrónico', blank=True, null = True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    codigo = models.CharField('Código',max_length=250, blank=False, null = False)
    descrip = models.CharField('Descripción',max_length=250, blank=False, null = False)
    um = models.CharField('Unidad de Medida',max_length=50, blank=False, null = False)
    precioCUP = models.DecimalField('Precio CUP', max_digits=18, decimal_places=5, null=False, blank=False)
    precioCL = models.DecimalField('Precio CL', max_digits=18, decimal_places=5, null=False, blank=False)
    habilitado = models.BooleanField('Artículo Activado/Artículo no Activado', default = True)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

    def __str__(self):
        return self.descrip
