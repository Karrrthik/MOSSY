import React from 'react'

export default function Mossy({ files }) {
  return (
      files.map(file => {
        return(
            <div key={file.id}>
            <p>{file.filename}</p>
            </div>
        )
    })
    )
}
