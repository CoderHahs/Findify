import React from 'react';
import './NameInput.css';

class NameInput extends React.Component {
    constructor(props) {
        super(props);
        this.state = { value: '' };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({ value: event.target.value });
    }

    handleSubmit(event) {
        document.getElementById('thanks').innerHTML = 'A name was submitted: ' + this.state.value;
        event.preventDefault();
    }

    render() {
        return (
            <div className="container">
                <div className="inner-container">
                    <form onSubmit={this.handleSubmit}>
                        <input type='text' id='name-input' value={this.state.value} onChange={this.handleChange}></input>
                        <input type="submit" value="Submit" on />
                    </form>
                    <h2 id='thanks'> </h2>
                </div>
            </div>
        );
    }
}


export default NameInput;