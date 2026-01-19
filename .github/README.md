# FluxCD Demo Application

The purpose of this repository is to act as a base for learning GitOps with FluxCD. You can edit anything and everything in this repository to experiment with deployments on our OKD cluster.

## Quick Start

### Step 1: Fork and Customize

1. Fork this repository to your own GitHub account
2. Clone your fork locally
3. Search and replace `PLACEHOLDER` throughout the repository with a descriptive name for your application (e.g., `<your-name>-demo-app`, `<your-name>-gitops`, etc.)
   - This will be your Docker repository name in ACR
   - Use lowercase and hyphens only

### Step 2: Set Up Azure Container Registry (ACR) Access

Before you can build and push Docker images, you need to configure GitHub secrets for ACR authentication.

1. **Create a Scope Map:**
   - Log into Azure Portal
   - Navigate to your ACR instance
   - Go to Repository permissions > Scope maps
   - Click "Add" to create a new scope map
   - Name it (e.g., `your-name-push-pull`)
   - Set Repository: `*` (wildcard for all repositories)
   - Grant permissions: `content/read`, `content/write`, `metadata/read`, `metadata/write`
   - Do NOT grant `content/delete` or `metadata/delete`
   - Save the scope map

2. **Create a Token linked to the Scope Map:**
   - Go to Repository permissions > Tokens
   - Click "Add" to create a new token
   - Name it (e.g., `your-name-token`)
   - Select the scope map you just created
   - Set status to "Enabled"
   - Click "Generate"
   - Copy the generated password immediately (it's only shown once!)
   - The username will be the token name

3. **Create GitHub Secrets:**
   - Go to your forked repository on GitHub
   - Navigate to Settings > Secrets and variables > Actions
   - Create the following secrets:
     - `ACR_REGISTRY`: Your ACR login server (e.g., `yourregistry.azurecr.io`)
     - `ACR_USERNAME`: The token name you created
     - `ACR_PASSWORD`: The token password you copied

### Step 3: Build and Push Your Images

1. Go to the Actions tab in your GitHub repository
2. Select "Build and Deploy" workflow
3. Click "Run workflow"
4. This will:
   - Automatically bump the version in `client/package.json`
   - Build Docker images for both frontend (client) and backend (server)
   - Push images to ACR with tags like `dev-v1.0.0`

### Step 4: Deploy to OKD Using FluxCD

Once your images are built and pushed to ACR:

1. Navigate to the FluxCD repository (link will be provided)
2. Use the provided templates to create:
   - Deployment manifests
   - Service manifests
3. Follow the deployment guide to configure your application
4. Commit and push your changes
5. FluxCD will automatically sync and deploy your application to the OKD cluster

## Comprehensive Documentation

For detailed information about GitOps, FluxCD, and our deployment processes, see the [comprehensive documentation](https://foundryspatial.atlassian.net/wiki/spaces/AKG/pages/2805399555/Foundry+Spatial+GitOps+-+FluxCD).

## Need Help?

- Review the written guide provided during the presentation
- Ask questions in the team channel
- Pair with experienced team members for your first deployment

## Experiment Freely

This is a learning environment. Feel free to:

- Modify the application code
- Change Docker configurations
- Experiment with different deployment strategies
- Break things and learn from the process
