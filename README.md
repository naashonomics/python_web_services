# python_web_services

Building a REST API using Python and Flask

1> Vanila Flask: pip install Flask

   python flask_test.py 
   
   curl -V http://127.0.0.1:5000/
   
   Default Content Type : text/html
   
   POST:
   curl -i -X POST -H "Content-Type: application/json" -d "{""data1"":""data goes here"",""data2"":""data2 goes here""}" 
   http://127.0.0.1:5000 
   
HTTP/1.0 201 CREATED

Content-Type: application/json

Content-Length: 86

Server: Werkzeug/0.15.2 Python/3.7.3

Date: Wed, 09 Oct 2019 00:30:09 GMT

{
 
 "yousent": {
 
   "data1": "data goes here",
   
   
   "data2": "data2 goes here"
  
  }
}

Multiplication:

curl  http://127.0.0.1:5000/multi/5

{

   "result": 50

}
   
   
2> Flask Extention: pip install Flask-RESTFul

