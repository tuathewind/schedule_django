from django.shortcuts import render
from .models import Group, Student, Teacher, Time, Class, Schedule
from django.views import generic, View
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    date_today = date.today()
    return render(
        request,
        'index.html',
        context={'date_today':date_today,}
    )

class ScheduleView(generic.ListView):
    model = Schedule
    template_name = 'index.html'

class StudentListView(LoginRequiredMixin, generic.ListView):
    model = Student
    paginate_by = 10

class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Student

class TeacherListView(LoginRequiredMixin, generic.ListView):
    model = Teacher
    paginate_by = 10

class TeacherDetailView(LoginRequiredMixin, generic.DetailView):
    model = Teacher

class GroupListView(LoginRequiredMixin, generic.ListView):
    model = Group
    paginate_by = 10


class ELoginView(View):

    # код метода get

    def post(self, request):
        # забираем данные формы авторизации из запроса
        form = AuthenticationForm(request, data=request.POST)

        # забираем IP адрес из запроса
        ip = get_client_ip(request)
        # получаем или создаём новую запись об IP, с которого вводится пароль, на предмет блокировки
        obj, created = TemporaryBanIp.objects.get_or_create(
            defaults={
                'ip_address': ip,
                'time_unblock': timezone.now()
            },
            ip_address=ip
        )

        # если IP заблокирован и время разблокировки не настало
        if obj.status is True and obj.time_unblock > timezone.now():
            context = create_context_username_csrf(request)
            if obj.attempts == 3 or obj.attempts == 6:
                # то открываем страницу с сообщением о блокировки на 15 минут при 3 и 6 неудачных попытках входа
                return render_to_response('accounts/block_15_minutes.html', context=context)
            elif obj.attempts == 9:
                # или открываем страницу о блокировке на 24 часа, при 9 неудачных попытках входа
                return render_to_response('accounts/block_24_hours.html', context=context)
        elif obj.status is True and obj.time_unblock < timezone.now():
            # если IP заблокирован, но время разблокировки настало, то разблокируем IP
            obj.status = False
            obj.save()

        # если пользователь ввёл верные данные, то авторизуем его и удаляем запись о блокировке IP
        if form.is_valid():
            auth.login(request, form.get_user())
            obj.delete()

            next = urlparse(get_next_url(request)).path
            if next == '/admin/login/' and request.user.is_staff:
                return redirect('/admin/')
            return redirect(next)
        else:
            # иначе считаем попытки и устанавливаем время разблокировки и статус блокировки
            obj.attempts += 1
            if obj.attempts == 3 or obj.attempts == 6:
                obj.time_unblock = timezone.now() + timezone.timedelta(minutes=15)
                obj.status = True
            elif obj.attempts == 9:
                obj.time_unblock = timezone.now() + timezone.timedelta(1)
                obj.status = True
            elif obj.attempts > 9:
                obj.attempts = 1
            obj.save()

        context = create_context_username_csrf(request)
        context['login_form'] = form

        return render_to_response('accounts/login.html', context=context)