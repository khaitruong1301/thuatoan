def two_sum(nums, target):
    # Tạo một từ điển để lưu trữ các giá trị đã xem qua
    seen = {}
    
    for i, num in enumerate(nums):
        # Tìm số cần thiết để hoàn thành cặp
        needed = target - num
        
        # Kiểm tra xem số cần thiết có trong từ điển không
        if needed in seen:
            # Trả về cặp chỉ số tìm thấy
            return [seen[needed], i]
        
        # Nếu chưa tìm thấy, thêm số hiện tại vào từ điển
        seen[num] = i
    
    # Trả về None nếu không tìm thấy cặp nào
    return None

# Ví dụ sử dụng
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)

print(result)  # Output: [0, 1] vì nums[0] + nums[1] = 2 + 7 = 9
