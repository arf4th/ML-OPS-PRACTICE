#!/bin/bash

skills=( Linux Git Docker Kubernetes AWS )

echo "first skill is ${skills[0]}"
echo "third skill is ${skills[2]}"
echo "all skills ${skills[*]}"
echo "number of skills are ${#skills[*]}"
newskills=( aws/terraform )

echo "new skills are ${newskills[*]}"