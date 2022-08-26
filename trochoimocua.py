print("bạn đang ở trong một căn phòng tối tăm nằm trong một lâu dài bí hiểm")
print("Có bon cánh cửa trước mặt bạn. Hãy chọn một cánh cửa để thám hiểm")
player_Choice = input("Hãy chọn 1, 2, 3, 4: ")

if player_Choice == "1":
    print("Bạn đã tìm thấy căn phòng chứa kho báu. Phát tài rồi")
    print("Bạn đã tháng cuộc. Trò chơi kết thúc")

elif player_Choice == "2":
    print("Cửa bật mở. Một tiểu yêu giận dữ lao ra và phang chùy vào đầu bạn.")
    print("Bạn đã thua. Trò chơi kết thúc")
elif player_Choice == "3":
    print("Bạn bước vào phòng này và thấy một con rồng đang ngủ say.")
    print("Bạn có thể: ")
    print("1: Thử trộm vàng của con rồng.")
    print("2: Thử đi vòng qua nó để tới cửa ra.")

    dragon_Choice = input("Nhập 1 hoặc 2: ")
    if dragon_Choice == "1":
        print("Con rồng đã thức giấc và sẽ nuốt chửng bạn.")
        print("Bạn đã thua và Trò chơi đã kết thúc.")
    elif dragon_Choice == "2":
        print("Bạn rón rén đi vòng qua con rồng và thoát khỏi tòa lâu đài. Xin chào ánh mắt trời.")
        print("Bạn đã chiến thắng! Trò chơi kết thúc tại đây.")
    else:
        print("Xin lỗi, bạn phải nhập 1 hoặc 2.")

else:
    print("Bạn đã không nhập đúng lựa chọn.")
    print("Vui lòng khởi động lại trò chơi.")
