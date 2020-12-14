from django.urls import reverse
# from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone


# Post.object.all()
class PostManager(models.Manager):
	def all(self, *args, **kwargs):
		return super(PostManager, self).filter(draft=False).filter(publish_lte=timezone.now())

# Create your models here.
def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)


class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to=upload_location, 
					null=True, 
					blank=True,
					width_field="width_field",
					height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field  = models.IntegerField(default=0)
	content = models.TextField()
	draft = models.BooleanField(default=0)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	
	# objects = PostManager()

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_obsolute_url(self):
		return reverse("posts:detail", kwargs={"slug": self.slug})
		# return "/posts/%s" %(self.id)


	class Meta:
		ordering = ["-timestamp", "-updated"]

def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

# appeding the ID of the instance
def pre_save_post_reciever(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_reciever, sender=Post)


class Images(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE,)
	image = models.ImageField(upload_to="upload_location",
		null=True,
		blank=True)

	def __str__(self):
		return self.post.title + "Image"

class Contact(models.Model):
	full_name = models.CharField(max_length=120)
	phone  = models.IntegerField()
	email = models.CharField(max_length=150)
	subject = models.CharField(max_length=200)
	message = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


	def __unicode__(self):
		return self.full_name

	def __str__(self):
		return self.full_name
