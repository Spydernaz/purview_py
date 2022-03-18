
echo "Creating Package"
# python3 -m pip install --upgrade build
python3 -m build

# python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*


pip3 install -i https://test.pypi.org/simple/ purview-py==0.0.3