from django.conf.urls import url,include
from .views import index,customers,customer_by_token,owner_login,\
    owner_page,logout,owner_account,customer_add,display_all_serials,\
    distribute,distribute_by_token,distribute_save,payment_save,\
    update,update_by_token,track_state,start_track,end_track,track_place



urlpatterns = [
    url(r'^$' , index , name=""),
    url(r'^customer/$' , customers , name="Customer"),
    url(r'customer/(?P<token>[0-9]+)/$' , customer_by_token , name="Customer"),
    url(r'owner/login' , owner_login , name="Login"),
    url(r'^owner/$' , owner_page , name="Owner"),
    url(r'logout' , logout , name="Logout"),
    url(r'owner/account' , owner_account , name="Account"),
    url(r'customer/add' , customer_add , name="CustomerAdd"),
    url(r'display/serials' , display_all_serials , name="Serials"),
    url(r'^distribute/$' , distribute , name="Distribute"),
    url(r'distribute/(?P<token>[0-9]+)/$' , distribute_by_token , name="Distribute"),
    url(r'^distribute_save/$', distribute_save ,name="saved"),
    url(r'^payment_save/$' , payment_save , name="saved"),
    url(r'update/(?P<token>[0-9]+)/$', update_by_token, name="Update"),
    url(r'^update/$', update , name="Update"),
    url(r'^track_state/$', track_state , name="Track"),
    url(r'^start_track/$', start_track , name = "start"),
    url(r'^end_track/$', end_track , name = "end"),
    url(r'^track/$' , track_place , name="track"),
]