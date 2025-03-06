import py3Dmol

pdb_code = '6DT1'  # Replace with your PDB code

viewer = py3Dmol.view(query='pdb:' + pdb_code)

# Other styles - Note: to do multiple styles do addStyle instead of setStyle
#viewer.setStyle({'cartoon': {'color':'spectrum'}})
viewer.setStyle({'sphere': {'radius':0.5}})
#viewer.setStyle({'line': {}})
#viewer.setStyle({'stick': {}})

#viewer.setStyle({'surface': {'opacity':0.8}}) # not working

viewer.zoomTo()

folder_path = 'SE Project - Nethya Liyanage/templates/'
# Save the visualization to an HTML file
with open(folder_path + 'protein_viewer.html', 'w') as f:
    f.write(viewer._make_html())
