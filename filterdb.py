# Hak Cipta (C) 2020-2021 oleh oke-retard@Github, < https://github.com/okay-retard >.
#
# File ini adalah bagian dari proyek < https://github.com/okay-retard/ZectUserBot >,
# dan dirilis di bawah "Perjanjian Lisensi GNU v3.0".
# Silakan lihat < https://github.com/okay-retard/ZectUserBot/blob/master/LICENSE >
#
# Seluruh hak cipta.

dari . impor klien

filter = cli["Aceng"]["FILTER"]


async def add_filters(kata kunci, chat_id, message_id) -> Tidak ada:
    tambahkan = menunggu filter.find_one({"keyword": kata kunci})
    jika menambahkan:
        tunggu filter.update_one(
            {"kata kunci": kata kunci},
            {"$set": {"chat_id": chat_id, "msg_id": message_id}},
        )
    kalau tidak:
        tunggu filter.insert_one(
            {"keyword": kata kunci, "chat_id": chat_id, "msg_id": message_id}
        )


async def del_filters(kata kunci, chat_id):
    menunggu filter.delete_one({"keyword": kata kunci, "chat_id": chat_id})


async def filter_info(kata kunci, chat_id):
    r = menunggu filter.find_one({"keyword": kata kunci, "chat_id": chat_id})
    jika r:
        kembali r
    kalau tidak:
        kembali Salah


async def filter_del(chat_id):
    menunggu filter.delete_many({"chat_id": chat_id})


async def all_filters(chat_id):
    r = [jo async untuk jo di filter.find({"chat_id": chat_id})]
    jika r:
        kembali r
    kalau tidak:
        kembali Salah
