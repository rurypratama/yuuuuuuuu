# Hak Cipta (C) 2020-2021 oleh oke-retard@Github, < https://github.com/okay-retard >.
#
# File ini adalah bagian dari proyek < https://github.com/okay-retard/ZectUserBot >,
# dan dirilis di bawah "Perjanjian Lisensi GNU v3.0".
# Silakan lihat < https://github.com/okay-retard/ZectUserBot/blob/master/LICENSE >
#
# Seluruh hak cipta.

impor motor.motor_asyncio
dari config impor MONGO_URI


cli = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
