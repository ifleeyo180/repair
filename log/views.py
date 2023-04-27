from django.shortcuts import render, get_object_or_404
from django.views.generic import *
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import LogItem, Tag
from .forms import LogItemForm
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
# 報修項目列表
'''
class LogList(UserPassesTestMixin, ListView):
  model = LogItem
  ordering = ['-id']
  paginate_by = 15

  def get_queryset(self):
        # Get the original queryset
        queryset = super().get_queryset()

        # Get the search query from request GET parameters
        search_query = self.request.GET.get('search', '')

        if search_query:
            # Check if the search query can be converted to an integer
            try:
               search_query_int = int(search_query)
               int_filter = Q(pk=search_query_int)
            except ValueError:
               int_filter = Q()

            # Apply the filter to the queryset using the Q object
            queryset = queryset.filter(
                Q(subject__icontains=search_query) |
                Q(reporter__icontains=search_query) |
                Q(handler__icontains=search_query) |
                Q(tags__subject__icontains=search_query) |
                int_filter
            ).distinct()

        return queryset
  
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['is_superuser'] = self.request.user.is_superuser
      return context

  def test_func(self):
      return self.request.user.is_authenticated
'''
      
# 檢視報修項目
class LogView(DetailView):
  model = LogItem

# 新增報修項目
class LogCreate(CreateView):
  model = LogItem
  # 新增時只顯示需填寫的部份欄位
  fields = ['subject', 'description', 'reporter', 'phone', 'picture']

  def get_success_url(self):
     return reverse('log_list')
  
  def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     context['tags'] = Tag.objects.all()
     return context
  
  def form_valid(self, form):
     selected_tag_id = self.request.POST.get('tags')
     selected_tag = get_object_or_404(Tag, id=selected_tag_id)
     log_item = form.save(commit=False)
     log_item.save()
     log_item.tags.add(selected_tag)
     return super().form_valid(form)

# 回覆維修進度
class LogReply(LoginRequiredMixin, UpdateView):
  model = LogItem
  #fields = ['handler', 'status', 'comment']
  form_class = LogItemForm
  template_name = 'log/logitem_detail.html'

  def get_success_url(self):
     return reverse('log_view', kwargs={'pk': self.object.id})
  
  # get_initial: 設定表單初始預設值
  def get_initial(self):
    data = {}
    # 取得目前登入的使用者資訊
    u = self.request.user
    # 如果有名字，就填名字，否則就填帳號名稱
    if u.first_name:
        data['handler'] = u.first_name
    else:
        data['handler'] = u.username
    return data

class LogDelete(LoginRequiredMixin, DeleteView):
   model = LogItem
   success_url= '/log'

   def test_func(self):
      return self.request.user.is_superuser
   
   def handle_no_permission(self):
      messages.error(self.request, '您沒有刪除報修項目的權限。')
      return HttpResponseRedirect(reverse('log_list'))
   


def index(request):
    return render(request, 'log/logitem_list.html')
