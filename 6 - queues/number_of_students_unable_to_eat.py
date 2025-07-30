import collections

def countStudents( students: list[int], sandwiches: list[int]) -> int:
        
        
        student_que = collections.deque()
        # student_que.popleft()

        for student in students: 
            student_que.append(student)

        students_fed = 0 
        counter = 0 
 
        for i in range(len(sandwiches)): 
            sandwichTaken = False 
            while counter < len(students) and not sandwichTaken:
                if student_que[0] == sandwiches[i]:
                    student_que.popleft()
                    counter = 0
                    students_fed += 1 
                    sandwichTaken = True 
                else:
                    if counter >= len(students):
                        break 
                    student_que.append(student_que.popleft()) 
                    counter += 1

        return len(students) - students_fed 


students = [1,1,0,0]
sandwiches = [0,1,0,1]


countStudents(students, sandwiches)