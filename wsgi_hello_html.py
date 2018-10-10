from wsgiref.simple_server import make_server

# Every WSGI application must have an application object - a callable
# object that accepts two arguments. For that purpose, we're going to
# use a function (note that you're not limited to a function, you can
# use a class for example). The first argument passed to the function
# is a dictionary containing CGI-style environment variables and the
# second variable is the callable object (see PEP 333).
def hello_world_app(environ, start_response):
    status = '200 OK'  # HTTP Status
    headers = [('Content-type', 'text/html; charset=utf-8')]  # HTTP Headers
    start_response(status, headers)

    # The returned object is going to be printed
    return [b"""<!DOCTYPE html>
<html>
<title>W3.CSS Template</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body>

<div class="w3-display-container" style="margin-bottom:50px">
  <img src="https://www.w3schools.com/w3images/beach3.jpg" style="width:100%">
  <div class="w3-display-bottomleft w3-container w3-amber w3-hover-orange w3-hide-small"
   style="bottom:10%;opacity:0.7;width:70%">
  <h2><b>4 Good Reasons<br>For travelling with us</b></h2>
</div>
</div>

<div class="w3-row w3-container" style="margin:50px 0">
<div class="w3-half w3-container">
  <div class="w3-topbar w3-border-amber">
    <img src="https://www.w3schools.com/w3images/cellphone.jpg" style="width:100%">
    <h2>Smart Vacation</h2>
    <p>Full vacation control from your cell phone.</p>
  </div>
</div>

<div class="w3-half w3-container">
  <div class="w3-topbar w3-border-amber">
    <img src="https://www.w3schools.com/w3images/sealions.jpg" style="width:100%">
    <h2>Super Offers</h2>
    <p>Up to 50% offers. Always 25% student offers.</p>
  </div>
</div>
</div>

<div class="w3-row w3-container" style="margin:50px 0">
<div class="w3-half w3-container">
  <div class="w3-topbar w3-border-orange">
    <img src="https://www.w3schools.com/w3images/truck.jpg" style="width:100%">
    <h2>Car Rental Included</h2>
    <p>Wherever you travel our car rental is included.</p>
  </div>
</div>

<div class="w3-half w3-container">
  <div class="w3-topbar w3-border-orange">
    <img src="https://www.w3schools.com/w3images/nowornever.jpg" style="width:100%">
    <h2>Realize Your Dreams</h2>
    <p>Don't wait until it is to late.</p>
    </div>
</div>
</div>

</body>
</html>"""]

with make_server('', 3000, hello_world_app) as httpd:
    print("Serving on port 3000...")

    # Serve until process is killed
    httpd.serve_forever()
