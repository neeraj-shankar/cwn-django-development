## Documentation on Django Views

### Introduction to DRF Views
#### DRF view classes are inherited from the View class of Django. DRF reduces the code amount needed
#### for REST interface creation and provides reusability.

### APIVIEW Class
#### APIView class is an important component of the DRF views by which the view class of Django is
#### sub-classed. APIView class works as the base for all the views selected by you in your application

#### function-based views:
##### Function can also be used for direct implementation of the APIView. @api_view decorator must be
##### used if view writing is through a function.

#### viewsets:
##### Viewset in Django is the combination of the logic of related views.

#### class-based views:
##### Alternative approach of implementing views as the objects of Python in place of functions is
##### provided by the class-based views

#### generic view classes:
##### Certain Built-in views are combined in the class Based Generic Views which are used for
##### implementing some functionalities such as Retrieve, Create, Delete, and Update.

#### mixins:
##### Those classes that commonly inherit from the objects are called mxins

### Explain How DRF Views Work
#### When the request comes to the view, firstly request object initialization is done by the view,
#### and the request object is the DRF-enhanced HttpRequest.

#### The following advantages are provided by it in comparison to HttpRequest of the Django:

##### Automatic parsing of content takes place according to the content-type header and it is represented as the request.data.

##### Patch and put methods are supported by it. (only GET and POST are the only methods allowed by Django).

##### Permissions are checked against the other methods of the HTTP on request by temporary method overriding.

#### After request instance creation, renderers and content negotiators are used by the view for storing accepted information in the request. 
#### Authentication is performed by the view after that and permission checking and throttling are performed.

#### Authentication simply determines the user, any error is not returned by it. Throttle and permissions check needed this information. 
#### There is a raising of NotAuthenticated exceptions in case of unsuccessful authentication. And in case the request 
#### is not permitted, then there is a raising of PermissionDenied exceptions. And if there is throttling of request at 
#### the time of throttling checking then the exception is raised whose name is a Throttled exception.
#### And there is no notification for the user about the waiting time for the request permission.

#### check_object_permissions and check_permissions are two parts of permission checking. General permission is covered 
#### **by the check_permissions** and it is called before the execution of the view handler. check_object_permissions is not
#### executed if APIView is extended you need to explicitly call it for execution. If ViewSets or Generic Views are used
#### then for the detail views there is a calling of check_object_permissions.

#### The request method is checked by the view of whether it is from one of the given methods below or not. This checking is done after checking the authentication, permissions/Authorization, and throttling.

1. get
2. put
3. post
4. head
5. patch
6. option
7. delete
8. trace

#### If the request method is one from the above, then it determines whether the method of the request
#### corresponds to any available methods in view and then executes it. A "MethodNotAllowed" error 
#### will be displayed if the method is not permitted or specified in the view that is being called.

### Policy Attributes
| Attribute              | Usage                                                                                      | Example                                    |
|------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------|
| renderer_classes       | It determines the type of media returned by the response.                                  | BrowsableAPIRenderer, JSONRenderer         |
| parser_classes	        | It determines which data parser is suitable for which media type.                          | FileUploadParser, JSONParser               |
| authentication_classes | Determines which authentication schemas must be used for user identification.              | SessionAuthentication, TokenAuthentication |
 | throttle_classes	      | It determines whether the request authorization is done according to the request rate.	    | UserRateThrottle, AnonRateThrottle         |
 | permission_classes	    | It determines whether the user credentials are used for the Authorization of the request.	 | DjangoModelPermissions, IsAuthenticated    |


