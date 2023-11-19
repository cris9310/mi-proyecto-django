from django.urls import path
from . import views
app_name = 'academico_app'

urlpatterns = [
    path(
        'create-user/',
        views.UserCreateView.as_view(),
        name='create-user'
    ),
    path(
        'dashboard/',
        views.Dashboard.as_view(),
        name='dashboard'
    ),
    path(
        'config',
        views.ConfigTemplateView.as_view(),
        name='config'
    ),
    path(
        'create-periodo/',
        views.PeriodoCreateView.as_view(),
        name='create-periodo'
    ),
    path(
        'list-periodo/',
        views.PeriodoListView.as_view(),
        name='list-periodo'
    ),
    path(
        'create-programas/',
        views.ProgramaCreateView.as_view(),
        name='create-programas'
    ),
    path(
        'list-program/',
        views.Programalistview.as_view(),
        name='list-program'
    ),
    path(
        'detail-program/<pk>/',
        views.ProgramaDetailView.as_view(),
        name='detail-program'
    ),
    path(
        'update-Program/<pk>/',
        views.ProgramaUpdateView.as_view(),
        name='update-Program'
    ),
    path(
        'delete-Program/<pk>/',
        views.ProgramaDeleteView.as_view(),
        name='delete-Program'
    ),
    path(
        'create-pensum',
        views.CrearPensum.as_view(),
        name='create-pensum'
    ),
    path(
        'list-teacher/create-teacher/',
        views.TeacherCreateView.as_view(),
        name='create-teacher'
    ),
    path(
        'list-teacher/',
        views.Teacherlistview.as_view(),
        name='list-teacher'
    ),
    path(
        'update-teacher/<pk>/',
        views.TeacherUpdateView.as_view(),
        name='update-teacher'
    ),
    path(
        'detail-teacher/<pk>/',
        views.TeacherDetailView.as_view(),
        name='detail-teacher'
    ),
    path(
        'list-teacher/topic-list/<pk>/',
        views.TeacherTopicsListview.as_view(),
        name='topic-list'
    ),
    path(
        'Habilit-teacher/<pk>/',
        views.TeacherHabilitView.as_view(),
        name='Habilit-teacher'
    ),
    path(
        'create-topic/',
        views.MateriasCreateView.as_view(),
        name='create-topic'
    ),
    path(
        'list-topic/',
        views.Materialistview.as_view(),
        name='list-topic'
    ),
    path(
        'update-topic/<pk>/',
        views.MateriaUpdateView.as_view(),
        name='update-topic'
    ),

    path(
        'delete-topic/<pk>/',
        views.MateriaDeleteView.as_view(),
        name='delete-topic'
    ),
    path(
        'update-pensum',
        views.Getpunsumview.as_view(),
        name='update-pensum'
    ),
    path(
        'create-inventario',
        views.InventarioCreateView.as_view(),
        name='create-inventario'
    ),
    path(
        'list-teacher/topic-list-notes/<pk>/',
        views.TeacherNotesListview.as_view(),
        name='topic-list-notes'
    ),
    path(
        'detail-topic/<pk>/',
        views.MateriaDetailView.as_view(),
        name='detail-topic'
    ),

    path(
        'delete-periodo/<pk>/',
        views.PeriodoDeleteView.as_view(),
        name='delete-periodo'
    ),
    path(
        'delete-teacher/<pk>/',
        views.TeacherDeleteView.as_view(),
        name='delete-teacher'
    ),

    path(
        'profile/',
        views.ProfileDetailView.as_view(),
        name='profile'
    ),

    path(
        'list-student/notes/<pk>/',
        views.Vernotas.as_view(),
        name='notes'
    ),

    path(
        'list-periodos-asignar/<pk>/',
        views.AsignamateriaPreviewView.as_view(),
        name='list-periodos-asignar'
    ),
    path(
        'list-student/',
        views.Studentlistview.as_view(),
        name='list-student'
    ),
    path(
        'list-student/list-student-cargue/',
        views.StudentCargueListview.as_view(),
        name='list-student-cargue'
    ),


    path(
        'detail-student/<pk>/',
        views.StudentDetailView.as_view(),
        name='detail-student'
    ),
    path(
        'update-student/<pk>/',
        views.StudentMasiveUpdateView.as_view(),
        name='update-student'
    ),
    path(
        'list-top-asignar',
        views.StudentAsigView.as_view(),
        name='list-top-asignar'
    ),
    path(
        'export-plant-student',
        views.export_users_csv,
        name='export-plant-student'
    ),
    path(
        'create-student/',
        views.StudentCreateView.as_view(),
        name='create-student'
    ),
    path(
        'list-student/list-top-graduado/',
        views.ListFinalily.as_view(),
        name='list-top-graduado'
    ),
    path(
        'delete-student/<pk>/',
        views.StudentDeleteView.as_view(),
        name='delete-student'
    ),
    path(
        'delete-student-finally/<pk>/',
        views.TeacherDeleteFinalView.as_view(),
        name='delete-student-finally'
    ),
    path(
        'asignacion',
        views.AsignamateriasCreateView.as_view(),
        name='asignacion'
    ),
    path(
        'agre-more/<pk>/',
        views.AddMateriasList.as_view(),
        name='agre-more'
    ),
    path(
        'list-top-a-graduar',
        views.GraduateView.as_view(),
        name='list-top-a-graduar'
    ),
    path(
        'list-graduated',
        views.GraduatedListView.as_view(),
        name='list-graduated'
    ),
    path(
        'habilitado',
        views.HabiliteTemplateView.as_view(),
        name='habilitado'
    ),
    path(
        'generar-cortes',
        views.GenerateCorteView.as_view(),
        name='generar-cortes'
    ),
    path(
        'expor-plant-est',
        views.Export_plant_est_csv.as_view(),
        name='expor-plant-est'
    ),
    path(
        'upload-notes',
        views.UpdateNotasView.as_view(),
        name='upload-notes'
    ),










]
