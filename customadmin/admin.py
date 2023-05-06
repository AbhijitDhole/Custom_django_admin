from django.contrib import admin
from .models import Blog
from django.utils.html import format_html
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    readonly_fields =['photo_tag']
    exclude = ()
    list_display= ['title', 'photo_tag', 'less_content', 'click_me', 'created_at', 'extra_title', 'tags'] 
    list_display_links = ['less_content', 'title']
    list_filter = ['is_deleted', 'created_at', 'extra_title']
    radio_fields = {'tags': admin.HORIZONTAL}
    save_on_top = True
    list_per_page = 2
    
    def less_content(self, obj):
        return format_html(f'<span style = "color:green">{obj.content[:100]}</span>')
    
    def click_me(self, obj):
       return format_html(f"<button><a href='/admin/customadmin/blog/{obj.id}/change/'>View</a></buttton>")
    
    def photo_tag(self, obj):
        return format_html(f'<img src="/media/{obj.image}" style="height:400px;width:300px;>')
        
admin.site.register(Blog, BlogAdmin)

