from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from models import MenuEntry
from models import BaseContent
from models import PathRedirect
from models import Masonry as MasonryModel
from models import Rubrique as RubriqueModel


class Base(TemplateView):

    def menu(self):
        if not hasattr(self, '_menu'):
            self._menu = MenuEntry.objects.all().order_by('position').filter(parent__slug='AFK13')
        return self._menu

    def get_context_data(self, *args, **kwargs):
        ctx = super(Base, self).get_context_data(*args, **kwargs)
        ctx['menu'] = self.menu()
        return ctx


class Masonry(Base):

    def masonry(self):
        if not hasattr(self, '_masonry'):
            self._masonry = get_object_or_404(MasonryModel, slug=self.kwargs['slug'])
        return self._masonry

    def get_context_data(self, *args, **kwargs):
        menu = self.menu()
        masonry = self.masonry()
        return dict(menu=menu, masonry=masonry)

    @property
    def template_name(self):
        return self.masonry().template_name


class Rubrique(Base):

    template_name = 'base/rubrique.html'

    def get_context_data(self, *args, **kwargs):
        menu = self.menu()
        rubrique = get_object_or_404(RubriqueModel, slug=self.kwargs['slug'])
        root = rubrique.get_root()
        return dict(root=root, rubrique=rubrique, menu=menu)


class Content(Base):

    template_name = 'base/content.html'

    def get_context_data(self, *args, **kwargs):
        menu = self.menu()
        content = get_object_or_404(BaseContent, slug=self.kwargs['slug'])
        return dict(menu=menu, content=content)


class Login(Base):

    template_name = 'base/login.html'


class Redirect(Base):

    template_name = 'base/login.html'

    def get(self, *args, **kwargs):
        slug = kwargs.pop('slug')
        path = get_object_or_404(PathRedirect, slug=slug).path
        return redirect(path)
