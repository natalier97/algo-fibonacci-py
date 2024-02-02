#F(n) = F(n-1) + F(n-2)
#starts w/ [0,1]
def fibonacci(n):
    #define base cases
  sequence = [0,1]
  newNum = 0
    #funct to create new_number
  for i in range(n+1):
    newNum = sequence[i] + sequence[i+1]
    #add new_number
    sequence.append(newNum)
    #return the nth Fibonacci Number
  return sequence[n]

print(fibonacci(7))
# function fibonacci(num) {
#   let sequence = [0,1];
#   let newNum = 0;
#   for (let i = 0; i <= num; i++){
#     newNum = sequence[i] + sequence[i+1];
#     sequence.push(newNum);
#   }
 
#   return sequence[num]
# }
# console.log(fibonacci(7))
