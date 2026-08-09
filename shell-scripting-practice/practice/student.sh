#!/bin/bash


echo "============ Student Report ============"

#asking student to enter his/her details

echo "enter your name"
read name
echo "enter your age"
read age
echo "enter your college"
read college
echo "enter your course"
read course
echo "enter your semester"
read semester


echo "enter your favorite three skills"
read skill1
read skill2
read skill3
echo "Favorite Skills
1. $skill1
2. $skill2
3. $skill3"

array=($skill1 $skill2 $skill3)

goal="future devops engineer"
echo "Career Goal : $goal"
echo "Goal length ${#goal}"
echo "first word ${goal[0]}"

echo "enter two marks from your two subjects"
read subject1
read subject2
echo "Marks
subject 1 : $subject1
subject 2 : $subject2
Total $((subject1 + subject2))"
Average $(((subject1 + subject2) / 2))"

echo "================================================="
