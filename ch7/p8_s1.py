height = [0,1,0,2,1,0,1,3,2,1,2,1]

def func(height):
  if not height:
    return 0
  
  volume = 0
  left = 0
  right = len(height) - 1
  left_max = height[left]
  right_max = height[right]

  """
  아래 코드는 코드 이해보다는 논리 이해가 더 필요합니다.
  왼쪽에 있는 a의 높이가 2이고 오른쪽에 있는 b의 높이가 3일때 a와 b 사이에서는 최소한 2까지 물이 차오르게 되어있습니다.
  아래에서는 이 a와 b를 각각 댐이라고 표현하겠습니다.
  """

  while left < right:
    left_max = max(height[left], left_max) # 새로 불러온 height[left]가 기존의 left_max보다 더 높으면 이 점이 새로운 왼쪽 댐이 됩니다.
    right_max = max(height[right], right_max) # 새로 불러온 height[right]가 기존의 right_max보다 더 높으면 이 점이 새로운 오른쪽 댐이 됩니다.
    if left_max <= right_max: # left_max가 right_max보다 낮을때 현재의 left_max보다 더 높은 새로운 left_max까지는 전부 현재 left_max까지 물이 차올라 있다고 가정할 수 있습니다.
      volume += left_max - height[left] # 최소한 right_max가 새로운 left_max라는 다음 댐이 될 수 있기 때문이죠.
      left += 1
    else:
      volume += right_max - height[right] # 오른쪽 역시 마찬가지입니다. 새로운 right_max가 나올때까지, 혹은 left_max와 만날때까지 현재 right_max만큼 물이 차있다고 가정할 수 있습니다.
      right -= 1
  return volume

print(func(height))
