import React, { useState } from 'react';
import {
    AppBar,
    Toolbar,
    Typography,
    Button,
    Container,
    Box,
    Card,
    CardContent,
    CardActions,
    Grid,
    Dialog,
    DialogTitle,
    DialogContent,
    IconButton,
    Drawer,
    List,
    ListItem,
    ListItemText
} from '@mui/material';
import { Close } from '@mui/icons-material';
import { useDataProvider } from 'react-admin';

const HighLight = () => {
    const [open, setOpen] = useState(false);
    const [dialogContent, setDialogContent] = useState(null);
    const [selectedResource, setSelectedResource] = useState('Airline');
    const dataProvider = useDataProvider();

    const resources = ['Airline', 'Airplane', 'Airport', 'Flight'];

    const handleCardClick = async () => {
        try {
            const { data } = await dataProvider.getList(selectedResource, {
                pagination: { page: 1, perPage: 1 },
                meta: { include: ['+all'] }
            });
            setDialogContent(data[0]);
            setOpen(true);
        } catch (error) {
            console.error('Error fetching data', error);
        }
    };

    const renderDialogContent = () => {
        if (!dialogContent) return null;
        return (
            <Box>
                <Typography variant="h6">{dialogContent.name || dialogContent.first_name || dialogContent.description}</Typography>
                {Object.entries(dialogContent)
                    .filter(([key]) => !['id', 'ja_type', 'attributes', 'relationships', 'meta'].includes(key))
                    .map(([key, value]) => (
                        <Typography key={key} variant="body2">
                            {key}: {value}
                        </Typography>
                    ))}
                {/* Render relationships */}
                {/* Example */}
                {dialogContent.AirplaneList && (
                    <Box mt={2}>
                        <Typography variant="body1" color="textSecondary">
                            Related Airplanes:
                        </Typography>
                        {dialogContent.AirplaneList.map((plane, index) => (
                            <Box key={index} p={1} border="1px solid #ccc" borderRadius="4px" mb={1}>
                                Model: {plane.model}, Capacity: {plane.seating_capacity}
                            </Box>
                        ))}
                    </Box>
                )}
            </Box>
        );
    };

    return (
        <div style={{ display: 'flex' }}>
            {/* Sidebar Drawer */}
            <Drawer variant="permanent" open={true}>
                <List>
                    {resources.map((resource) => (
                        <ListItem button key={resource} onClick={() => setSelectedResource(resource)}>
                            <ListItemText primary={resource} />
                        </ListItem>
                    ))}
                </List>
            </Drawer>

            {/* Main Content */}
            <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
                <AppBar position="static" sx={{ marginBottom: '1em', bgcolor: 'purple' }}>
                    <Toolbar>
                        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                            My App
                        </Typography>
                        <Button color="inherit">Login</Button>
                    </Toolbar>
                </AppBar>

                <Container>
                    <Typography variant="h4" component="h1" gutterBottom>
                        Welcome to My App
                    </Typography>

                    {/* Clickable Card */}
                    <Card onClick={handleCardClick} sx={{ cursor: 'pointer', bgcolor: 'purple.50' }}>
                        <CardContent>
                            <Typography variant="h5" component="div">
                                {selectedResource}
                            </Typography>
                            <Typography variant="body2" color="text.secondary">
                                Click to view details and related resources.
                            </Typography>
                        </CardContent>
                        <CardActions>
                            <Button size="small">Learn More</Button>
                        </CardActions>
                    </Card>

                    {/* Grid for extra layout */}
                    <Grid container spacing={2} mt={2}>
                        <Grid item xs={12} sm={6}>
                            <Box bgcolor="primary.main" color="primary.contrastText" p={2} textAlign="center">
                                Grid Item 1
                            </Box>
                        </Grid>
                        <Grid item xs={12} sm={6}>
                            <Box bgcolor="secondary.main" color="secondary.contrastText" p={2} textAlign="center">
                                Grid Item 2
                            </Box>
                        </Grid>
                    </Grid>
                </Container>

                {/* Dialog for details */}
                <Dialog open={open} onClose={() => setOpen(false)} fullWidth>
                    <DialogTitle>
                        {selectedResource} Details
                        <IconButton
                            aria-label="close"
                            onClick={() => setOpen(false)}
                            sx={{ position: 'absolute', right: 8, top: 8, color: (theme) => theme.palette.grey[500] }}
                        >
                            <Close />
                        </IconButton>
                    </DialogTitle>
                    <DialogContent>{renderDialogContent()}</DialogContent>
                </Dialog>
            </Box>
        </div>
    );
};

export default HighLight;