# rm */__pycache__/api*
# rm */__pycache__/models*
# rm */__pycache__/serializers*

echo "Eliminando migraciones"
rm helptutor/*/migrations/00*.py
rm helptutor/*/migrations/__pycache__/00*.pyc

echo "Generando carpetas migrations en modulos de apps"
cd helptutor/advertisements
mkdir migrations
cd migrations
touch __init__.py
cd ..
cp -r migrations ../knowledge_areas
cp -r migrations ../payments
cp -r migrations ../places
cp -r migrations ../schedules
cp -r migrations ../services
cp -r migrations ../sesions
cp -r migrations ../users
echo "¡Exito!"
