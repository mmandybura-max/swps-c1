#!/usr/bin/env bash

echo "Bez tokena"
curl "http://localhost:8000/api/osoby/?type=json"

echo -e "\n\nPoprawny token"
curl -H "Authorization: Token 556f8e5fae604b51fa750876f1b394890e0ab270" "http://localhost:8000/api/osoby/?type=json"

echo -e "\n\nNiepoprawny token"
curl -H "Authorization: Token 556f8e5fae604b51fa750876f1b394890e0ab271" "http://localhost:8000/api/osoby/?type=json"

echo -e "\n"