
# ==========================
# BÀI 1: Chuyển đổi nhiệt độ
# ==========================
def chuyen_doi_nhiet_do(do_c):
    return do_c * 9/5 + 32


# ================================
# BÀI 2: Giải phương trình bậc nhất
# ================================
def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    else:
        x = -b / a
        return f"Nghiệm của phương trình là x = {x}"


# =====================================
# BÀI 3: Kiểm tra số Armstrong bậc 3
# =====================================
def kiem_tra_so_armstrong(n):
    tong = sum(int(ch) ** 3 for ch in str(n))
    return tong == n


# ===========================
# BÀI 4: Tính giai thừa
# ===========================
def tinh_giai_thua(n):
    if n < 0:
        return None
    gt = 1
    for i in range(1, n+1):
        gt *= i
    return gt


# =====================================
# BÀI 5: Kiểm tra số nguyên tố
# =====================================
def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# =====================================
# BÀI 6: Tạo dãy Fibonacci
# =====================================
def day_fibonacci(n):
    if n <= 0:
        return []
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]


# =====================================
# BÀI 7: Tính tổng số hoàn hảo
# =====================================
def la_so_hoan_hao(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

def tinh_tong_so_hoan_hao(a, b):
    return sum(n for n in range(a, b+1) if la_so_hoan_hao(n))


# =====================================
# BÀI 8: Tìm số lẻ lớn nhất
# =====================================
def tim_so_le_lon_nhat(a, b, c):
    le = [x for x in (a, b, c) if x % 2 != 0]
    return max(le) if le else -1


# =====================================
# BÀI 9: Đệ quy tính tổng chữ số
# =====================================
def tinh_tong_chu_so(n):
    if n < 10:
        return n
    return n % 10 + tinh_tong_chu_so(n // 10)


# =====================================
# BÀI 10: Đệ quy Fibonacci
# =====================================
def tim_so_fibonacci(n):
    if n <= 1:
        return n
    return tim_so_fibonacci(n-1) + tim_so_fibonacci(n-2)


# =====================================
# BÀI 11: Lambda - tích 3 số
# =====================================
tich_ba_so = lambda a, b, c: a * b * c


# =====================================
# BÀI 12: Lambda - kiểm tra số chẵn
# =====================================
kiem_tra_chan = lambda n: n % 2 == 0


# =====================================
# BÀI 13: Lambda - kiểm tra số dương
# =====================================
kiem_tra_duong = lambda n: n > 0


# =====================================
# BÀI 14: Lambda - tổng 2 số
# =====================================
tong_hai_so = lambda a, b: a + b


# =====================================
# BÀI 15: In số nguyên tố trong khoảng 100-500
# =====================================
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

cac_so_nguyen_to_100_500 = [x for x in range(100, 501) if la_nguyen_to(x)]
