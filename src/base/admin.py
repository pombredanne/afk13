import compositeadmin as admin

from models import User
from models import Article
from models import Rubrique
from models import MenuEntry
from models import Publication
from models import Masonry
from models import TextWithLink
from models import PathRedirect


admin.site.register(User)
admin.site.register(Masonry)
admin.site.register(Article)
admin.site.register(Rubrique)
admin.site.register(MenuEntry)
admin.site.register(Publication)
admin.site.register(TextWithLink)
admin.site.register(PathRedirect)
