import React, {MouseEvent} from 'react'

const DoubleClickButton: React.FC = () => {
    const clickHandler = (e: MouseEvent<HTMLButtonElement>) => {
        if(e.detail===2){
            console.info("Doule-clicked")
        }
    }

    return(
        <button onClick={clickHandler}>
            click me
        </button>
    )
}