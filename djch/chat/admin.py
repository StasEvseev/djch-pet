from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Room


class RoomProxy(Room):
    class Meta:
        proxy = True

    def link_to_open_chat(self):
        url = reverse('chat:chat', kwargs={'id': self.id})
        return format_html('<a href="{url}" target="_blank">{url}</a>', url=url)


admin.site.register(
    RoomProxy,
    list_display=["id", "title", "staff_only", "link_to_open_chat"],
    list_display_links=["id", "title"],
)
