from django.contrib import admin

import nested_admin

from .models import Person, Nuc, DetectedInformation

# Register your models here.

class PersonInline(nested_admin.NestedStackedInline):
    model = Person
    extra = 0
    readonly_fields = ['image_tag', ]


class NucAdmin(nested_admin.NestedModelAdmin):
    model = Nuc
    exclude = ()
    inlines = [PersonInline]

admin.site.register(Nuc, NucAdmin)


class DetectedInformationInline(nested_admin.NestedStackedInline):
    model = DetectedInformation
    feilds = ['person', 'image', 'image_tag', 'detected_nuc', 'time', 'match_rate', ]
    readonly_fields = ['image_tag', 'time', ]
    extra = 0


class PersonAdmin(nested_admin.NestedModelAdmin):
    model = Person
    exclude = ()
    readonly_fields = ['image_tag', ]
    inlines = [DetectedInformationInline]

    

admin.site.register(Person, PersonAdmin)




class DetectedInformationAdmin(nested_admin.NestedModelAdmin):
    model = DetectedInformation
    exclude = ()
    readonly_fields = ['image_tag', 'time', ]

# admin.site.register(DetectedInformation, DetectedInformationAdmin)
admin.site.register(DetectedInformation, DetectedInformationAdmin)