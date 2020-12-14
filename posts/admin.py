from django.contrib import admin
# Register your models here.

from .models import Post, Contact


class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated","timestamp"]
	list_display_links = ["updated"]
	list_editable = ["title"]
	list_filter = ["updated", "timestamp"]
	search_fields = ["title", "content"]
	class Meta:
		model = Post

class ContactAdmin(admin.ModelAdmin):
	list_display = [
		"full_name",
		"phone",
		"email",
		"timestamp",
	]


# this is the in built function which register post model into admin sites.
admin.site.register(Post, PostModelAdmin) 
admin.site.register(Contact, ContactAdmin)


