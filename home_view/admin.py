from django.contrib import admin

# Register your models here.


from .models import PessoaFisica, PessoaJuridica # Substitua pelo seu modelo

admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)
