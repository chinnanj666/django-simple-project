from django.http import HttpResponse

def hello_world(request):
    # Simple HTML response
    html = """
   <html>
    <head><title>Hello World</title></head>
    <body>
        <!-- Center the text inside the <h1> -->
        <h1 style="background-color: aqua; text-align: center;">Hello, World!</h1>
        <p style="text-align: center;">Welcome to Django!</p>
    </body>
</html>

    """
    return HttpResponse(html)
# # views.py
# from django.shortcuts import render

# def hello_world(request):
#     return render(request, 'index.html')
