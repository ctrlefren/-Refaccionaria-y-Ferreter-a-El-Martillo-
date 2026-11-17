from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Curso
from .forms import CursoForm
from .models import Curso, Profesor
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib import messages

class CustomLoginView(LoginView):
    template_name = 'cursos/registration/login.html'

    def form_valid(self, form):
        messages.info(self.request, f"¡Bienvenido de nuevo, {form.get_user().username}!")
        return super().form_valid(form)
class CursoListView(ListView):
    model = Curso
    template_name = 'cursos/lista.html'
    context_object_name = 'cursos'
    paginate_by = 6
    ordering = ['nombre']
    
# 2. DETALLE DE CURSO (Reemplaza a detalle_curso FBV)
class CursoDetailView(DetailView):
    model = Curso
    template_name = 'cursos/detalle.html'
    context_object_name = 'curso'

# 3. CREAR CURSO (Reemplaza a crear_curso FBV)
class CursoCreateView(LoginRequiredMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/formulario.html'
    success_url = reverse_lazy('web_lista_cursos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Nuevo Curso (CBV)'
        return context

# 4. EDITAR CURSO (Reemplaza a editar_curso FBV)
class CursoUpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/formulario.html'
    success_url = reverse_lazy('web_lista_cursos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = f'Editar Curso: {self.object.nombre}'
        return context

# 5. ELIMINAR CURSO (Nueva funcionalidad CRUD)
class CursoDeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = 'cursos/curso_confirm_delete.html'
    success_url = reverse_lazy('web_lista_cursos')
    context_object_name = 'curso'

class ProfesorDetailView(DetailView):
    model = Profesor
    template_name = 'cursos/profesor_detalle.html'
    context_object_name = 'profesor'
    paginate_by = 3

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Curso
from .forms import CursoForm

# 1. LISTA DE CURSOS CON PAGINACIÓN
class CursoListView(ListView):
    model = Curso
    template_name = 'cursos/lista.html'
    context_object_name = 'cursos'
    paginate_by = 6  # Muestra máximo 6 cursos por página

class CursoDetailView(DetailView):
    model = Curso
    template_name = 'cursos/detalle.html'
    context_object_name = 'curso'

# 2. CREACIÓN CON MENSAJE FLASH
class CursoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/formulario.html'
    success_url = reverse_lazy('web_lista_cursos')
    success_message = "¡El curso '%(nombre)s' fue creado exitosamente!"

# 3. EDICIÓN CON MENSAJE FLASH
class CursoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'cursos/formulario.html'
    success_url = reverse_lazy('web_lista_cursos')
    success_message = "¡El curso '%(nombre)s' fue actualizado correctamente!"

# 4. ELIMINACIÓN CON MENSAJE FLASH
class CursoDeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = 'cursos/curso_confirm_delete.html'
    success_url = reverse_lazy('web_lista_cursos')
    context_object_name = 'curso'

    def delete(self, request, *args, **kwargs):
        curso = self.get_object()
        messages.warning(self.request, f"El curso '{curso.nombre}' fue eliminado del sistema.")
        return super().delete(request, *args, **kwargs)

    
class ProfesorListView(ListView):
    model = Profesor
    template_name = 'cursos/profesores_lista.html'
    context_object_name = 'profesores'
    paginate_by = 3  
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Estudiante
from .forms import EstudianteForm

# 1. LISTA DE ESTUDIANTES (Paginada)
class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'cursos/estudiantes_lista.html'
    context_object_name = 'estudiantes'
    paginate_by = 5

# 2. DETALLE DE ESTUDIANTE
class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = 'cursos/estudiante_detalle.html'
    context_object_name = 'estudiante'

# 3. CREAR ESTUDIANTE (Protegido + Mensaje Flash)
class EstudianteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'cursos/estudiante_formulario.html'
    success_url = reverse_lazy('web_lista_estudiantes')
    success_message = "¡El estudiante '%(nombre)s %(apellido)s' fue registrado con éxito!"

# 4. EDITAR ESTUDIANTE
class EstudianteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'cursos/estudiante_formulario.html'
    success_url = reverse_lazy('web_lista_estudiantes')
    success_message = "¡Los datos del estudiante '%(nombre)s' fueron actualizados correctamente!"

# 5. ELIMINAR ESTUDIANTE
class EstudianteDeleteView(LoginRequiredMixin, DeleteView):
    model = Estudiante
    template_name = 'cursos/estudiante_confirm_delete.html'
    success_url = reverse_lazy('web_lista_estudiantes')
    context_object_name = 'estudiante'

    def delete(self, request, *args, **kwargs):
        estudiante = l.get_object()
        messages.warning(self.request, f"El estudiante '{estudiante.nombre} {estudiante.apellido}' fue eliminado.")
        return super().delete(request, *args, **kwargs)



# 1. LISTA PAGINADA
class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'cursos/estudiantes_lista.html'
    context_object_name = 'estudiantes'
    paginate_by = 5
    ordering = ['apellido', 'nombre']


# 2. DETALLE (con cursos inscritos y cursos disponibles)
class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = 'cursos/estudiante_detalle.html'
    context_object_name = 'estudiante'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos_inscritos'] = Curso.objects.filter(estudiantes=self.object)
        context['cursos_disponibles'] = Curso.objects.exclude(estudiantes=self.object)
        return context


# 3. CREAR
class EstudianteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'cursos/estudiante_formulario.html'
    success_url = reverse_lazy('web_lista_estudiantes')
    success_message = "¡El estudiante '%(nombre)s %(apellido)s' fue registrado con éxito!"


# 4. EDITAR
class EstudianteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'cursos/estudiante_formulario.html'
    success_url = reverse_lazy('web_lista_estudiantes')
    success_message = "¡Los datos del estudiante '%(nombre)s' fueron actualizados correctamente!"


# 5. ELIMINAR
class EstudianteDeleteView(LoginRequiredMixin, DeleteView):
    model = Estudiante
    template_name = 'cursos/estudiante_confirm_delete.html'
    success_url = reverse_lazy('web_lista_estudiantes')
    context_object_name = 'estudiante'

    def form_valid(self, form):
        messages.warning(
            self.request,
            f"El estudiante '{self.object.nombre} {self.object.apellido}' fue eliminado."
        )
        return super().form_valid(form)