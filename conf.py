import os

os.system(  'cd build \
          && git clone https://github.com/opencor/sphinx-theme theme \
          && cp ../src/conf.py . \
          && echo "copyright = u\'2011-$2019, University of Auckland\'\nhtml_theme = \'theme\'\nhtml_show_sphinx = False\nhtml_show_copyright = False" >> conf.py \
          && sphinx-build -q -b html -c . ../src html \
          && python theme/cmake/stringreplace.py html/_static/theme.css "103, 103, 103" "54, 96, 146" \
          && python theme/cmake/appendfile.py html/_static/theme.css ../styles/opencor.css \
          && python theme/cmake/appendfile.py html/_static/pygments.css ../styles/cellmlText.css')
