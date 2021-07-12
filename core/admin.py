from django.contrib import admin
from .models import Cargo, Funcionario, Servico


# Register your models here.

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['cargo', 'ativo', 'modificado']


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['servico', 'icone', 'modificado', 'ativo']


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cargo', 'modificado', 'ativo']
