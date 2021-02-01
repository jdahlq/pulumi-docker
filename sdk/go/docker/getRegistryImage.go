// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package docker

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Reads the image metadata from a Docker Registry. Used in conjunction with the
// [docker\_image](https://www.terraform.io/docs/providers/docker/r/image.html) resource to keep an image up
// to date on the latest available version of the tag.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-docker/sdk/v2/go/docker"
// 	"github.com/pulumi/pulumi-docker/sdk/v2/go/docker/"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		opt0 := "ubuntu:precise"
// 		ubuntuRegistryImage, err := docker.LookupRegistryImage(ctx, &docker.LookupRegistryImageArgs{
// 			Name: &opt0,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = docker.NewRemoteImage(ctx, "ubuntuRemoteImage", &docker.RemoteImageArgs{
// 			Name: pulumi.String(ubuntuRegistryImage.Name),
// 			PullTriggers: pulumi.StringArray{
// 				pulumi.String(ubuntuRegistryImage.Sha256Digest),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupRegistryImage(ctx *pulumi.Context, args *LookupRegistryImageArgs, opts ...pulumi.InvokeOption) (*LookupRegistryImageResult, error) {
	var rv LookupRegistryImageResult
	err := ctx.Invoke("docker:index/getRegistryImage:getRegistryImage", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getRegistryImage.
type LookupRegistryImageArgs struct {
	// The name of the Docker image, including any tags. e.g. `alpine:latest`
	Name *string `pulumi:"name"`
}

// A collection of values returned by getRegistryImage.
type LookupRegistryImageResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id           string  `pulumi:"id"`
	Name         *string `pulumi:"name"`
	Sha256Digest string  `pulumi:"sha256Digest"`
}
