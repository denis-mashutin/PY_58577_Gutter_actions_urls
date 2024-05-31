## Tested

## Issues
**A. [Normal]** The term 'application' is not consistent with Django applications. 
For example, when I click **Show all endpoints of application** in my_app.urls, I'd expect to see all endpoints in the application. Path? (Revise texts)
**B. [Major]** Only GET method for Django function-based views, even with ``require_POST`` decorator
**C. [Normal]** Why showing gutter icon with '/' path for every urlpatterns and router assignment?
**D. []** No **Generate request** for a router URL, although it's available in **Show all endpoints**
**E. []** For Flask routers, only ``url_prefix`` is taken into account, while there can be additional route elements defined in the router file

[//]: # (**C. []** POST method is not suggested for Django classes, when there's explicit ``get`` method)