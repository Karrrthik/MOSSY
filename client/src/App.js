 import React,{useState, useRef, useEffect} from 'react';
 import Mossy from "./Mossy";
 import axios from 'axios';
 import {v4 as uuid} from 'uuid';

const LOCAL_STORAGE_KEY = 'file.files'

function App() {
  const [file, UploadFile] = useState([]);
  const fileref = useRef();
  const Userowner = useRef();

  useEffect(() => {
    const storedFiles = localStorage.getItem(LOCAL_STORAGE_KEY);
    if (storedFiles) UploadFile(JSON.parse(storedFiles));
  }, []);

  useEffect(() => {
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(file));
  }, [file]);

  function fileupload(e){
    const thisfile = fileref.current.files[0];
    const owner = Userowner.current.value;
    console.log(thisfile.name);
    console.log(owner)
    if (thisfile.name) UploadFile(uploadedfile => [{id: uuid(), owner: owner, filename: thisfile.name, ufile: thisfile}]);
    axios.post('http://localhost:8000/upload', {file: file})
    .then(res => console.log(res.data))
    fileref.current.value = null;
  }

  return (
    <div>
      <input ref={Userowner} type="text"/>
      <input ref={fileref} type="file" />
      <button onClick={fileupload}>Upload</button>
      <Mossy files={file}/>
    </div>
  );
}

export default App;