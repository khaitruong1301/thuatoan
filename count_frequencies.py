def count_frequencies(lst):
    # Tạo một từ điển trống để lưu trữ tần suất của mỗi phần tử
    frequency = {}

    # Duyệt qua từng phần tử trong danh sách đầu vào
    for item in lst:
        # Đối với mỗi phần tử, tăng tần suất của nó lên 1.
        # Sử dụng phương thức get() để lấy giá trị hiện tại của key (phần tử),
        # nếu key không tồn tại, trả về giá trị mặc định là 0.
        frequency[item] = frequency.get(item, 0) + 1

    # Trả về từ điển tần suất sau khi đã duyệt qua tất cả các phần tử
    return frequency
