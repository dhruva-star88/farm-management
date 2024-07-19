from django.shortcuts import render
from .models import CropDetails, AssignmentDetails, WorkerDetails, EquipmentDetails, SupplierDetails, TaskHistory
from datetime import date
from django.db.models import Count
import json
from django.shortcuts import render, redirect, get_object_or_404

def dashboard(request):
    # Get counts for At A Glance section
    crop_count = CropDetails.objects.count()
    task_count = AssignmentDetails.objects.count()
    worker_count = WorkerDetails.objects.count()

    # Get counts for equipment status
    equipment_status_counts = EquipmentDetails.objects.values('status').annotate(count=Count('status'))
    available_count = 0
    unavailable_count = 0
    for status_count in equipment_status_counts:
        if status_count['status'] == 'available':
            available_count = status_count['count']
        elif status_count['status'] == 'un_available':
            unavailable_count = status_count['count']

    # Get lists of available and unavailable equipment
    available_equipments = EquipmentDetails.objects.filter(status='available')
    unavailable_equipments = EquipmentDetails.objects.filter(status='un_available')

    # Get total number of suppliers
    supplier_count = SupplierDetails.objects.count()

    # Get most recent supplier
    most_recent_supplier = SupplierDetails.objects.order_by('-id').first()

    # Get list of all suppliers
    suppliers = SupplierDetails.objects.all()

    # Get equipment and supplier details
    equipment_supplier_details = EquipmentDetails.objects.select_related('supplied_by').all()[:8]

    # Get current production information
    current_crops = CropDetails.objects.filter(planting_date__lte=date.today(), harvesting_date__gte=date.today())
    
    # Get urgent and upcoming tasks
    urgent_tasks = AssignmentDetails.objects.filter(end_date__lte=date.today()).order_by('end_date')[:3]
    upcoming_tasks = AssignmentDetails.objects.filter(end_date__gt=date.today()).order_by('end_date')[:3]
    all_urgent_tasks = AssignmentDetails.objects.filter(end_date__lte=date.today()).order_by('end_date')
    all_upcoming_tasks = AssignmentDetails.objects.filter(end_date__gt=date.today()).order_by('end_date')

    # Prepare data for pie chart (crop distribution)
    crop_distribution = CropDetails.objects.values('crop').annotate(count=Count('crop'))

    # Prepare data for bar graph (tasks by status)
    task_distribution = AssignmentDetails.objects.values('task').annotate(count=Count('task'))
    crop_distribution_data = list(crop_distribution)
    task_distribution_data = list(task_distribution)

    context = {
        'crop_count': crop_count,
        'task_count': task_count,
        'worker_count': worker_count,
        'current_crops': current_crops,
        'urgent_tasks': urgent_tasks,
        'upcoming_tasks': upcoming_tasks,
        'all_urgent_tasks': all_urgent_tasks,
        'all_upcoming_tasks': all_upcoming_tasks,
        'available_count': available_count,
        'unavailable_count': unavailable_count,
        'supplier_count': supplier_count,
        'most_recent_supplier': most_recent_supplier,
        'equipment_supplier_details': equipment_supplier_details,
        'available_equipments': available_equipments,
        'unavailable_equipments': unavailable_equipments,
        'suppliers': suppliers,
        'crop_distribution':  json.dumps(crop_distribution_data),
        'task_distribution': json.dumps(task_distribution_data),
    }
    return render(request, 'dashboard.html', context)

def complete_task(request, task_id):
    task = get_object_or_404(AssignmentDetails, pk=task_id)

    # Save task details to history table
    TaskHistory.objects.create(
        task=task.task,
        start_date=task.start_date,
        end_date=task.end_date,
        completed_by=task.assigned_to,  # Adjust fields as per your AssignmentDetails model
    )

    # Delete task from AssignmentDetails
    task.delete()

    # Redirect to task history page
    return redirect('dashboard')

def task_history(request):
    # Retrieve and display completed task history
    completed_tasks = TaskHistory.objects.all()
    context = {
        'completed_tasks': completed_tasks
    }
    return render(request, 'task_history.html', context)

def crop(request):
    crops = CropDetails.objects.all()
    return render(request, 'crop.html', {'crops': crops})

def task(request):
    assignments = AssignmentDetails.objects.all()
    return render(request, 'task.html', {'assignments': assignments})

def inventory(request):
    return render(request, 'inventory.html')

def worker(request):
    workers = WorkerDetails.objects.all()
    return render(request, 'worker.html', {'workers': workers})

def equipment(request):
    equipments = EquipmentDetails.objects.all()
    return render(request, 'equipment.html', {'equipments': equipments})

def supplier(request):
    suppliers = SupplierDetails.objects.all()
    return render(request, 'supplier.html', {'suppliers': suppliers})
