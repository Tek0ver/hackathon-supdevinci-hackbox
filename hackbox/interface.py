import streamlit as st
from list_tests import *

def start_tests(wanted_tests):
    for id, params in wanted_tests:
        for test in tests:
            if test["id"] == id:
                print(f"==============Starting test {test['id']}.==============")
                if params:
                    print(f"[LOG] Lancement du test avec les parametres suivants {params}")
                    test["command"](*params)
                else:
                    test["command"]()
                print(f"================Test {test['id']} ended.================")

if 'running_tests' not in st.session_state:
    st.session_state['running_tests'] = False

st.title("Test(s) à faire:")

wanted_tests = [] # list of tuples like (test_id, [parameters])

# Displays the list of tests and select wanted tests
for test in tests:
    current_params = []
    current_test = []
    checkbox = st.checkbox(test["title"])
    if checkbox:
        current_test = test["id"]
    if test["description"]:
        with st.caption(f"Description du test \"{test['title']}\"."):
            st.info(test["description"])
    if test['parameter'] and checkbox:
        for parameter in test['parameter']:
            if parameter[1] == 'int':
                current_params.append(int(st.number_input(parameter[0], value=parameter[2])))
            elif parameter[1] == 'str':
                current_params.append(str(st.text_input(parameter[0], value=parameter[2])))
    
    if current_test:
        wanted_tests.append((current_test, current_params))

# Displays the button to start tests and manages the tests
if st.session_state['running_tests'] is False and wanted_tests:
    if st.button("Lancer le test"):
        st.session_state['running_tests'] = True
        st.experimental_rerun()
elif st.session_state['running_tests']:
    st.info("Tests lancés.")
    with st.spinner("Tests en cours..."):
        start_tests(wanted_tests)
    st.success('Tests terminés.')
else:
    pass
