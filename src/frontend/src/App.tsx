import './App.css';

import Navigation from './components/navbar';
import SignIn from './components/auth';

function App() {
    return (
        <div className="App">
            <Navigation/>
            <SignIn/>
        </div>
    );
}

export default App;
