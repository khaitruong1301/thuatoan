def longestConsecutive(nums):
    if not nums:
        return 0  # Nếu mảng rỗng, trả về 0

    num_set = set(nums)  # Chuyển mảng thành set để loại bỏ trùng lặp và tăng tốc độ truy vấn
    longest_streak = 0   # Khởi tạo biến để lưu trữ độ dài chuỗi liên tục dài nhất

    for num in num_set:
        if num - 1 not in num_set:
            # Nếu không tìm thấy phần tử trước đó trong set, đây có thể là điểm bắt đầu của một chuỗi liên tục mới
            current_num = num
            current_streak = 1  # Khởi tạo chuỗi liên tục hiện tại

            # Tìm chuỗi liên tục bằng cách kiểm tra các phần tử tiếp theo
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1  # Tăng đếm khi tìm thấy phần tử liên tiếp

            # Cập nhật độ dài lớn nhất của chuỗi liên tục nếu cần
            longest_streak = max(longest_streak, current_streak)

    return longest_streak  # Trả về độ dài chuỗi liên tục dài nhất tìm được

# Định nghĩa mảng
nums = [100, 4, 200, 1, 3, 2]

# Gọi hàm và in kết quả
result = longestConsecutive(nums)
print("Độ dài chuỗi liên tục dài nhất là:", result)