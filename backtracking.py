def backtrack(nums, path, res):
    # Tambahkan subset saat ini ke hasil
    res.append(path[:])
    
    # Iterasi melalui bilangan yang tersisa
    for i in range(len(nums)):
        # Tambahkan bilangan ke subset saat ini
        path.append(nums[i])
        
        # Rekursif: coba semua kombinasi yang mungkin dengan tambahan ini
        backtrack(nums[i+1:], path, res)
        
        # Backtrack: hapus bilangan terakhir untuk mencoba kombinasi berikutnya
        path.pop()

def subsets(nums):
    res = []
    backtrack(nums, [], res)
    return res

# Contoh penggunaan
nums = [1, 2, 3]
print("Subsets dari", nums, "adalah:")
print(subsets(nums))
