from django.contrib import admin
from .models import CropDetails, EquipmentDetails, SupplierDetails, AssignmentDetails, WorkerDetails, TaskHistory

@admin.register(CropDetails)
class CropModel(admin.ModelAdmin):
    pass

@admin.register(EquipmentDetails)
class EquipmentModel(admin.ModelAdmin):
    pass

@admin.register(SupplierDetails)
class SupplierModel(admin.ModelAdmin):
    pass

@admin.register(AssignmentDetails)
class TaskModel(admin.ModelAdmin):
    pass

@admin.register(WorkerDetails)
class WorkerModel(admin.ModelAdmin):
    pass

@admin.register(TaskHistory)
class TaskHistoryModel(admin.ModelAdmin):
    pass