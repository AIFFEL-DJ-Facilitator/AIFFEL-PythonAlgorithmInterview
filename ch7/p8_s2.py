def func(height):
  stack = []
  volume = 0
  """
  stack 구조는 약간 복잡할 수 있으니 해당 코드를 실행하여 인풋데이터가 들어갔을때 어떻게 나오는지 확인하거나 동영상을 시청하는 것을 추천합니다.
  https://www.youtube.com/watch?v=hOIQ28oI1tc
  """

  for i in range(len(height)):
    #print(i)
    #print('input : ', height[i])
    while stack and height[i] > height[stack[-1]]:
      # 첫 인풋이 들어가면 stack이 false기 때문에 바로 while문이 종료됩니다.
      # 이후 새로운 인풋 데이터가 stack에 저장된 것보다 낮으면 계속 쌓입니다.
      #print('stack : ', stack)
      top = stack.pop()
      # 인풋 데이터가 stack에 저장된 것보다 높으면, 즉, 데이터가 증가하는 방향으로 바뀌면, 혹은 벽이 높아지면 앞서 쌓인 stack을 자신보다 높은 것이 등장하기 전까지 하나씩 불러옵니다.
      # 즉, 오른쪽의 벽을 기준으로 왼쪽에 해당 높이까지 쌓인 물을 계산할 수 있게 됩니다.
      #print('top : ', top)

      if not len(stack):
        break
      
      distance = i - stack[-1] -1 # 오른쪽 기준이 되는 벽으로부터 왼쪽의 벽(기준 벽과 같거나 낮은 벽)까지의 거리를 구하고
      #print('distance', distance)
      waters = min(height[i], height[stack[-1]]) - height[top] # 오른쪽 벽과 왼쪽 벽 중 낮은 것을 기준으로 바닥면의 높이를 제거합니다.(더 옴폭한 부분은 이전에 계산됩니다.)
      volume += distance * waters # 벽 간의 길이와 계산에 포함되는 물의 깊이를 곱해줍니다.
      #print('volume : ', volume)
      #print('')
    stack.append(i)
    #print('append : ', height[i])
    #print('stack : ', stack)
    
  
  return volume

print(func(height))

