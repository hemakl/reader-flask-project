#!/bin/bash

echo "Running 21 tests for manual observation.."
echo " "
echo " "
echo ".POST-ing new user Fox Mulder, OUTPUT=created"
echo "(curl -i -X POST -H 'Content-Type: application/json' -d '{"firstname":"Fox","lastname":"Mulder","email":"mulder@fbi.gov","password":"TrustNo1"}' http://127.0.0.1:5000/users)"
curl -i -X POST -H 'Content-Type: application/json' -d '{"firstname":"Fox","lastname":"Mulder","email":"mulder@fbi.gov","password":"TrustNo1"}' http://127.0.0.1:5000/users
echo " "
echo " "
echo "..POST-ing new user Dana Scully, OUTPUT=created"
echo "(curl -i -X POST -H 'Content-Type: application/json' -d '{"firstname":"Dana","lastname":"Scully","email":"scully@fbi.gov","password":"BeyondTheSea"}' http://127.0.0.1:5000/users)"
curl -i -X POST -H 'Content-Type: application/json' -d '{"firstname":"Dana","lastname":"Scully","email":"scully@fbi.gov","password":"BeyondTheSea"}' http://127.0.0.1:5000/users
echo " "
echo " "
echo "..POST-ing new user Melvin Frohike, OUTPUT=create"
echo "(curl -i -X POST -H 'Content-Type: application/json' -d '{"firstname":"Melvin","lastname":"Frohike","email":"frohike@tlg.org","password":"TrustDana"}' http://127.0.0.1:5000/users)"
curl -i -X POST -H 'Content-Type: application/json' -d '{"firstname":"Melvin","lastname":"Frohike","email":"frohike@tlg.org","password":"TrustDana"}' http://127.0.0.1:5000/users
echo " "
echo " "
echo "..GET-ing all users, OUTPUT=retrieves Mulder, Scully, and Frohike"
echo "(curl -i -X GET http://127.0.0.1:5000/users)"
curl -i -X GET http://127.0.0.1:5000/users
echo " "
echo " "
echo "..PUT-ing, firstname = Mel, for Frohike (wrong password!), OUTPUT=failed auth"
echo "(curl -i -X PUT -H 'Content-Type: application/json' -d '{"firstname":"Mel","lastname":"Frohike","email":"frohike@tlg.org","password":"TrustNo1"}' http://127.0.0.1:5000/users/3)"
curl -i -X PUT -H 'Content-Type: application/json' -d '{"firstname":"Mel","lastname":"Frohike","email":"frohike@tlg.org","password":"TrustNo1"}' http://127.0.0.1:5000/users/3
echo " "
echo " "
echo "..PUT-ing, firstname = Mel, for Frohike, OUTPUT=success"
echo "(curl -i -X PUT -H 'Content-Type: application/json' -d '{"firstname":"Mel","lastname":"Frohike","email":"frohike@tlg.org","password":"TrustDana"}' http://127.0.0.1:5000/users/3)"
curl -i -X PUT -H 'Content-Type: application/json' -d '{"firstname":"Mel","lastname":"Frohike","email":"frohike@tlg.org","password":"TrustDana"}' http://127.0.0.1:5000/users/3
echo " "
echo " "
echo "..GET-ing user Frohike, OUTPUT=retrieves Frohike, shows new firstname"
echo "(curl -i -X GET http://127.0.0.1:5000/users/3)"
curl -i -X GET http://127.0.0.1:5000/users/3
echo " "
echo " "
echo "..POST-ing new book for Frohike (Hitchhiker's Guide), OUTPUT=created"
echo "(curl -i -X POST -H 'Content-Type: application/json' -d '{"title":"Hitchhikers Guide","author":"Douglas Adams","isbn":"978-1400052929","publication_date":"Aug 3 2004"}' http://127.0.0.1:5000/users/3/books)"
curl -i -X POST -H 'Content-Type: application/json' -d '{"title":"Hitchhikers Guide","author":"Douglas Adams","isbn":"978-1400052929","publication_date":"Aug 3 2004"}' http://127.0.0.1:5000/users/3/books
echo " "
echo " "
echo "..GET-ing all books for Frohike, OUTPUT=1 book"
echo "(curl -i -X GET http://127.0.0.1:5000/users/3/books)"
curl -i -X GET http://127.0.0.1:5000/users/3/books
echo " "
echo " "
echo "..DELETE-ing user Frohike, OUTPUT=success"
echo "(curl -i -X DELETE http://127.0.0.1:5000/users/3)"
curl -i -X DELETE http://127.0.0.1:5000/users/3
echo " "
echo " "
echo "..GET-ing all users, OUTPUT=retrieves Fox, Dana (poor Frohike)"
echo "(curl -i -X GET http://127.0.0.1:5000/users)"
curl -i -X GET http://127.0.0.1:5000/users
echo " "
echo " "
echo "..POST-ing new book, Hitchhiker's Guide, for Mulder, OUTPUT=created"
echo "(curl -i -X POST -H 'Content-Type: application/json' -d '{"title":"Hitchhikers Guide","author":"Douglas Adams","isbn":"978-1400052929","publication_date":"Aug 3 2004"}' http://127.0.0.1:5000/users/1/books)"
curl -i -X POST -H 'Content-Type: application/json' -d '{"title":"Hitchhikers Guide","author":"Douglas Adams","isbn":"978-1400052929","publication_date":"Aug 3 2004"}' http://127.0.0.1:5000/users/1/books
echo " "
echo " "
echo "..POST-ing new book, All the President's Men, for Mulder, OUTPUT=created"
echo "(curl -i -X POST -H 'Content-Type: application/json' -d '{"title":"All the Presidents Men","author":"Bernstein and Woordward","isbn":"978-1476770512","publication_date":"Jun 3 2014"}' http://127.0.0.1:5000/users/1/books)"
curl -i -X POST -H 'Content-Type: application/json' -d '{"title":"All the Presidents Men","author":"Bernstein and Woordward","isbn":"978-1476770512","publication_date":"Jun 3 2014"}' http://127.0.0.1:5000/users/1/books
echo " "
echo " "
echo "..GET-ing all books for Mulder, OUTPUT=2 books"
echo "(curl -i -X GET http://127.0.0.1:5000/users/1/books)"
curl -i -X GET http://127.0.0.1:5000/users/1/books
echo " "
echo " "
echo "..GET-ing one book, Hitchhiker's Guide, for Mulder, OUTPUT=Hitchhiker's Guide"
echo "(curl -i -X GET http://127.0.0.1:5000/users/1/books/2)"
curl -i -X GET http://127.0.0.1:5000/users/1/books/2
echo " "
echo " "
echo "..PUT-ing, title = Hitchhiker's Guide to the Galaxy, for Hitchhiker's Guide, OUTPUT=success"
echo "(curl -i -X PUT -H 'Content-Type: application/json' -d '{"title":"Hitchhikers Guide to the Galaxy","author":"Douglas Adams","isbn":"978-1400052929","publication_date":"Aug 3 2004"}' http://127.0.0.1:5000/users/1/books/2)"
curl -i -X PUT -H 'Content-Type: application/json' -d '{"title":"Hitchhikers Guide to the Galaxy","author":"Douglas Adams","isbn":"978-1400052929","publication_date":"Aug 3 2004"}' http://127.0.0.1:5000/users/1/books/2
echo " "
echo " "
echo "..GET-ing one book, Hitchhiker's Guide, for Mulder, OUTPUT=retrieves Guide, shows new title"
echo "(curl -i -X GET http://127.0.0.1:5000/users/1/books/2)"
curl -i -X GET http://127.0.0.1:5000/users/1/books/2
echo " "
echo " "
echo "..DELETE-ing one book, All the President's Men, for Mulder, OUTPUT=success"
echo "(curl -i -X DELETE http://127.0.0.1:5000/users/1/books/3)"
curl -i -X DELETE http://127.0.0.1:5000/users/1/books/3
echo " "
echo " "
echo "..GET-ing one book, All the President's Men, for Mulder, OUTPUT=no book found"
echo "(curl -i -X GET http://127.0.0.1:5000/users/1/books/3)"
curl -i -X GET http://127.0.0.1:5000/users/1/books/3
echo " "
echo " "
echo "..DELETE-ing all books for Mulder, OUTPUT=success"
echo "(curl -i -X DELETE http://127.0.0.1:5000/users/1/books)"
curl -i -X DELETE http://127.0.0.1:5000/users/1/books
echo " "
echo " "
echo "..GET-ing all books for Mulder, OUTPUT=no books found"
echo "(curl -i -X GET http://127.0.0.1:5000/users/1/books)"
curl -i -X GET http://127.0.0.1:5000/users/1/books
echo " "
echo " "
echo Done!
