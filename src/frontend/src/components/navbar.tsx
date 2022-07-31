import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';

function Navigation() {
    return (
        <Navbar bg="light" expand="xl">
        <Container>
            <Navbar.Brand href="#home">the twilter project</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
                <Nav.Link href="#home">home</Nav.Link>
                <Nav.Link href="#link">about</Nav.Link>
                <Nav.Link href="#link">graph</Nav.Link>
                <NavDropdown title="explore" id="basic-nav-dropdown">
                <NavDropdown.Item href="#action/3.1">stats</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.2">
                    highlights
                </NavDropdown.Item>
                <NavDropdown.Item href="#action/3.3">twitter wrapped</NavDropdown.Item>
                </NavDropdown>
            </Nav>
            </Navbar.Collapse>
        </Container>
        </Navbar>
    );
}


export default Navigation;